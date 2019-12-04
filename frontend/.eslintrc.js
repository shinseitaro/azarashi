module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/essential', '@vue/prettier'],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'prettier/prettier': [
      'warning',
      {
        singleQuote: true,
        trailingComma: 'es5',
        semi: false,
        useTabs: false,
      },
    ],
    semi: "off",
    indent: "off",
  },
};
