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
    keyframes: {
      loadIn: {
        '0%': { transform: 'translateY(-5%)',
                opacity: 0 },
        '100%': { transform: 'translateY(0)',
                  opacity: 1 },
      },
      pulse: {
        '0%, 100%': { opacity: 1 },
        '50%': { opacity: 0.5 }
      },
    },
    animation: {
      'loadIn': 'loadIn 0.6s ease-out',
      'popup': 'loadIn 0.3s ease-out',
      'pulse': 'pulse 1.2s ease-in-out infinite'
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