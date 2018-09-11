const path = require('path');
const webpack = require('webpack');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  context: __dirname,

  entry: {
    main: './src/scripts/index',
    styles: './src/scripts/styles',
    loginStyles: './src/scripts/loginStyles'
  },

  output: {
    path: path.resolve('./bundles/'),
    filename: '[name].bundle.js',
  },

  mode: 'development',

  plugins: [
    new VueLoaderPlugin(),
  ],

  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      },
      {
        test: /\.sass$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: { // Allows sass within .vue files
              indentedSyntax: true
            },
          },
        ]
      },
      {
        test: /\.(svg|png|jpg|jpeg)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
              fallback: 'file-loader',
              quality: 50,
              name: 'images/[hash]-[name].[ext]',
            },
          },
        ],
      },
      {
        test: /\.vue$/,
        use: 'vue-loader',
      },
      {
        test: /\.(png|jpg|jpeg)$/,
        use: [
          {
            loader: 'file-loader',
          },
        ],
      },
    ],
  },
  resolve: {
    alias: {
      vue: 'vue/dist/vue.js', // for dev
      // vue: 'vue/dist/vue.common', // for production
    },
  },
};
