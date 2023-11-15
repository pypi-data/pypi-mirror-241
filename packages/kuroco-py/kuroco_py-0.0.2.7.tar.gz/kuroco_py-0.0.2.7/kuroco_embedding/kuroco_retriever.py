import asyncio

from dataclasses import dataclass
from typing import List, Union, Tuple
from pydantic import Extra
from langchain.schema.retriever import BaseRetriever
from langchain.schema.document import Document
from langchain.docstore.document import Document

THRESHOLD = 0.8

PROCESSING_TYPES: tuple = ("query", "topics_recommandation", "classification", "keywords_global", "keywords_per_topics")
@dataclass
class KurocoRetriever (BaseRetriever, extra=Extra.allow):
    """
    KurcoRetriever is a retriever that uses KurocoEmbedding to search for similar documents, topics recommendations, classifications or keywords search.
    It is designed to be used in Langchain.

    It requires a KurocoEmbedding instance and a list of relevant columns to search for.

    Extra Attributes:
        _embedder (KurocoEmbedding): The KurocoEmbedding object used for embedding requests
        _relevant (list): The list of relevant columns to search for
        _threshold (float): The threshold score for the similarity search
        _processing_type (str): The processing type of the retriever
        _limit (int): The maximum number of results to return

    Examples:
        >>> from kuroco import KurocoAPI, KurocoEmbedding
        >>> k_api = KurocoAPI.load_from_file(path='kuroco.json')
        >>> k_emb = KurocoEmbedding(('Shops', 'Zones'), k_api)
        >>> k_retriever = KurocoRetriever(k_emb, 'subject')
        >>> def format_docs(docs):
        >>>     return "\n\n".join([d.page_content for d in docs])
        >>> chain = (
        >>>     {"context": k_retriever | format_docs, "question": RunnablePassthrough()}
        >>>     | prompt
        >>>     | model
        >>>     | StrOutputParser()
        >>> )
        >>> chain.invoke("query")

    """
    _embedder: 'KurocoEmbedding'
    _relevant: list
    _threshold: float
    _limit: Union[int, None]

    def __init__(self, 
                 k_emb: 'KurocoEmbedding', 
                 relevant: Union[List[str], Tuple[str], str], 
                 threshold: float = THRESHOLD, 
                 limit: Union[int, None] = None, 
                 processing_type: str = "query"):
        BaseRetriever.__init__(self)

        self.embedder = k_emb

        assert isinstance(relevant, (list, tuple, str)), "Relevant must be a list, tuple or string"
        self.relevant = relevant
        
        assert isinstance(threshold, float) and 0 <= threshold <= 1, "Threshold must be a float between 0 and 1"
        self.threshold = threshold

        assert isinstance(limit, int) or limit is None, "Limit must be an integer or None"
        self.limit = limit

        self._processing_type = processing_type

    @property
    def processing_type(self):
        return self._processing_type
    
    @processing_type.setter
    def processing_type(self, value):
        assert value in PROCESSING_TYPES, f"Processing type must be one of {PROCESSING_TYPES}"
        self._processing_type = value

    def _get_relevant_documents(
        self, query: str, *, run_manager
    ) -> List[Document]:
        """
        Returns a list of `Document` objects that are relevant to the given `query`.
        The relevance is determined by a similarity search performed by the `embedder`
        object stored in the `metadata` dictionary. The search is limited to `limit`
        results and a `threshold` score. Only the columns specified in the `relevant`
        list of the `metadata` dictionary are considered for the search. The resulting
        `Document` objects have their `page_content` set to the relevant text and their
        `metadata` set to a dictionary containing the source of the document (`kuroco`)
        and the name of the relevant column.
        
        Args:
            query (str): The query string to search for.
            run_manager: A run manager object.
            
        Returns:
            List[Document]: A list of `Document` objects that are relevant to the query.
        """
        loop = asyncio.new_event_loop()
        if self.processing_type == "topics_recommandation":
            results = loop.run_until_complete(self.embedder.recommend_topics(query, limit=self.limit, with_score=False, threshold=self.threshold))
        elif self.processing_type == "classification":
            if isinstance(query, dict):
                subjects, query = query["subjects"], query["labels"]
            else:
                subjects = None
            results = loop.run_until_complete(self.embedder.zero_shot_topics_classification(query, with_score=False))
            if subjects:
                results = results[results["subject"].isin(subjects)]
        elif self.processing_type == "keywords_global":
            results = loop.run_until_complete(self.embedder.keywords_search_global(query, with_score=False))
        elif self.processing_type == "keywords_per_topics":
            results = loop.run_until_complete(self.embedder.keywords_search_per_topics(query, with_score=False))
        elif self.processing_type == "query":
            results = loop.run_until_complete(self.embedder.similarity_search(query, limit=self.limit, with_score=False, threshold=self.threshold))
        else:
            raise ValueError(f"Processing type {self.processing_type} is not supported")
        loop.close()
        # If no relevant column is asked, then transform all the dataframe into a list of documents
        selected_columns = [col for col in self.relevant if col in results.columns] if self.relevant else results.columns
        return [Document(page_content=w, 
                         metadata={"source": "kuroco", 
                                    "field": selected_columns[i]})
                        for v in results.loc[:, selected_columns].values.tolist()
                        for i, w in enumerate(v) if w
                ]
    