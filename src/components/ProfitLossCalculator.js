import React, { useState } from 'react';

const ProfitLossCalculator = () => {
  const [buyPrice, setBuyPrice] = useState('');
  const [sellPrice, setSellPrice] = useState('');
  const [amount, setAmount] = useState('');
  const [result, setResult] = useState('');

  const handleCalculate = () => {
    const profitLoss = (sellPrice - buyPrice) * amount;
    setResult(profitLoss.toFixed(2));
  };

  return (
    <div className="profit-loss-calculator">
      <h3>Profit/Loss Calculator</h3>
      <input
        type="number"
        placeholder="Buy Price"
        value={buyPrice}
        onChange={(e) => setBuyPrice(e.target.value)}
      />
      <input
        type="number"
        placeholder="Sell Price"
        value={sellPrice}
        onChange={(e) => setSellPrice(e.target.value)}
      />
      <input
        type="number"
        placeholder="Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button onClick={handleCalculate}>Calculate</button>
      {result && <p>Your profit/loss is: ${result}</p>}
    </div>
  );
};

export default ProfitLossCalculator;
