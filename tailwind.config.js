/** @type {import('tailwindcss').Config} */

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    borderWidth: {
      DEFAULT: '1px',
      '0': '0',
      '2': '2px',
      '3': '3px',
      '4': '4px',
      '6': '6px',
      '8': '8px'
    },
    colors: {
      background: {
        primary: '#191919',
        secondary: '#060606',
        tertiary: '#2F2F2F'
      },
      t: {
        primary: '#FFFFFF',
        secondary: '#A9A9A9',
        tertiary: '#191919'
      },
      bt: {
        primary: "#13DD63",
        secondary: "#37ed7f"
      }
    },
    extend: {
      fontFamily: {
        'sans': ['"Inter"', ...require('tailwindcss/defaultTheme').fontFamily.sans],
        'akshar': ['"Akshar"', '"Inter"', ...require('tailwindcss/defaultTheme').fontFamily.sans]
      }
    },
  },
  plugins: [],
}