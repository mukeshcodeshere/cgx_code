import React, { useEffect, useState } from 'react';
import axios from 'axios';

const NewsFeed = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    // Replace 'YOUR_API_KEY' with your actual News API key
    axios
      .get('https://newsapi.org/v2/everything?q=cryptocurrency&apiKey=YOUR_API_KEY')
      .then(response => {
        setNews(response.data.articles);
      })
      .catch(error => {
        console.error('Error fetching news:', error);
      });
  }, []);

  return (
    <div className="news-feed">
      <h2>Crypto News</h2>
      <ul>
        {news.map((article, index) => (
          <li key={index}>
            <a href={article.url} target="_blank" rel="noopener noreferrer">
              <h3>{article.title}</h3>
              <p>{article.description}</p>
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsFeed;
