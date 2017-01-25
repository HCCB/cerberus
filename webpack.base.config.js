var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
var srcPath = path.resolve("./src/assets/");
var cssPath = path.resolve("./src/assets/css/");
var scssPath = path.resolve("./src/assets/sass/");

var ExtractTextPlugin = require("extract-text-webpack-plugin");
// var CommonsPlugin = new require("webpack/lib/optimize/CommonsChunkPlugin")

module.exports = {
  context: __dirname,
  root: srcPath,
  // entry: "./src/assets/js/index",
  entry: {
    'main': "./src/assets/js/main/index",
    'docs': "./src/assets/js/docs/index",
  },

  output: {
      // path: path.join(__dirname, "js"),
      path: path.resolve("./src/assets/bundles/"),
      filename: "[name].js",
      chunkFilename: "[name]-[id].js"
      // allChunks: true
  },

  plugins: [
      new ExtractTextPlugin("[name].css"),
      //new CommonsPlugin({
      // minChunks: 3,
      // name: "common"
      //})
  ], // add all common plugins here

  module: {
    loaders: [
      {
        test: /\.jsx?$/, exclude: /(node_modules|bower_components)/, loader: 'babel' 
      },
      { 
        test: /\.css$/, 
        loader: ExtractTextPlugin.extract("style", ["css", "autoprefixer"])
      },  
      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract("style", ["css", "sass"])
      },
      {
        test: /\.txt$/,
        loader: "raw-loader",
      }, 
      {
        test: /\.(png|jpg|jpeg|gif|svg|woff|woff2)$/,
        loader: "url-loader?limit=10000",
      }, 
      {
        test: /\.(eot|ttf|wav|mp3)$/,
        loader: "file-loader",
      }
    ] // add all common loaders here
  },
  sassLoader: {
    includePath: [scssPath]
  },

  resolve: {
    modulesDirectories: [
        "node_modules",
        "bower_components",
        srcPath,
        cssPath,
        scssPath,
    ],
    extensions: ["", ".js", ".jsx", "css", "sass", "scss"]
  },
  debug: true
}
