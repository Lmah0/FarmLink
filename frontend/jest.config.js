module.exports = {
    "verbose": true,
    "moduleFileExtensions": ["js", "jsx", "css"],
    "testMatch": ["<rootDir>/tests/**/*.test.{js,jsx}"],
    "transform": {
      "^.+\\.jsx?$": "babel-jest"
    },
    "setupFilesAfterEnv": ["@testing-library/jest-dom/extend-expect"],
    "moduleNameMapper": {
      "\\.(css|less)$": "<rootDir>/tests/mockCss.js"
    },
    "testEnvironment": "jsdom" // Specify JSDOM as the test environment
  }
  