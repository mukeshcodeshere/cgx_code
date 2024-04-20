/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        body: ["Nunito"],
      },
      colors: {
        cyan: "#14ffec",
        purple: "#8a2be2",
        teal: "#008080",
        indigo: "#4b0082",
        orange: "#ff7f00",
      },
      fontSize: {
        xs: "12px",
        sm: "14px",
        base: "16px",
        lg: "18px",
        xl: "24px",
        "2xl": "32px",
        "3xl": "48px",
        "4xl": "64px",
        "5xl": "96px",
      },
    },
  },
};
