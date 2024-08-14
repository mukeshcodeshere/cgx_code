import React, { useState } from 'react';

const Watchlist = () => {
  const [watchlist, setWatchlist] = useState([]);
  const [newCoin, setNewCoin] = useState('');

  const handleAddToWatchlist = () => {
    if (newCoin && !watchlist.includes(newCoin)) {
      setWatchlist([...watchlist, newCoin]);
      setNewCoin('');
    }
  };

  const handleRemoveFromWatchlist = (coin) => {
    setWatchlist(watchlist.filter(item => item !== coin));
  };

  return (
    <div className="watchlist">
      <h3>Watchlist</h3>
      <input
        type="text"
        placeholder="Add coin"
        value={newCoin}
        onChange={(e) => setNewCoin(e.target.value)}
      />
      <button onClick={handleAddToWatchlist}>Add</button>
      <ul>
        {watchlist.map((coin, index) => (
          <li key={index}>
            {coin}
            <button onClick={() => handleRemoveFromWatchlist(coin)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Watchlist;
