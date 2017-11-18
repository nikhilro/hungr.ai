var path = require("path"),
    webpack = require("webpack"),
    ExtractTextPlugin = require("extract-text-webpack-plugin"),
    ManifestRevisionPlugin = require("manifest-revision-webpack-plugin")

var root = "./assets"

module.exports = {
    entry: {
        app_js: [
            root + "/scripts/app.js"
        ],
        main_css: [
            root + "/styles/main.scss"
        ],
        style_css: [
          root + "/styles/styles.css"
        ]
    },
    output: {
        path: path.join(__dirname, "app/public"),
        publicPath: "/assets/",
        filename: "[name].[chunkhash].js",
        chunkFilename: "[id].[chunkhash].chunk"
    },
    resolve: {
        extensions: [".js", ".jsx", ".scss", ".css"]
    },
    module: {
        loaders: [
            {
                test: /\.js$/i,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test: /\.scss$/i,
                loader: ExtractTextPlugin.extract("css-loader!sass-loader")
            },
            {
              test: /\.css$/i,
              loader: 'style-loader'
            },
            {
              test: /\.css$/i,
              loader: 'css-loader'
            },
            {
              test: /\.jsx?$/i,
              loader: 'babel-loader',
              exclude: /node_modules/,
              query:
                {
                  presets:['react', 'env', 'stage-1']
                }
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin("[name].[chunkhash].css"),
        new ManifestRevisionPlugin(path.join("app", "manifest.json"), {
            rootAssetPath: root,
            ignorePaths: ["/styles", "/scripts"]
        }),
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.NoEmitOnErrorsPlugin(),
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"'
            }
        }),
        new webpack.NoEmitOnErrorsPlugin()
    ]
}
