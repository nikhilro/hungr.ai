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
        bootstrap_js: [
            root + "/scripts/bootstrap.js"
        ],
        jquery_js: [
            root + "/scripts/jquery.1.8.3.min.js"
        ],
        jquery_ease_js: [
            root + "/scripts/jquery.easing.1.3.js"
        ],
        jquery_isotope_js: [
            root + "/scripts/jquery.isotope.js"
        ],
        classie_js: [
            root + "/scripts/classie.js"
        ],
        main_css: [
            root + "/styles/main.scss"
        ],
        styles_css: [
          root + "/styles/styles.css"
        ],
        bootstrap_css: [
          root + "/styles/bootstrap.css"
        ],
        font_awesome_css: [
          root + "/styles/font-awesome.css"
        ],
        responsive_css: [
          root + "/styles/responsive.css"
        ],
        animate_css: [
          root + "/styles/animate.css"
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
              use: ['css-hot-loader'].concat(ExtractTextPlugin.extract({
                fallback: 'style-loader',
                use: 'css-loader'
              })),
            },
            {
              test: /\.(ttf|otf|eot|svg|woff)$/i,
              loader: 'file-loader'
            },
            {
              test: /\.jsx?$/i,
              loader: 'babel-loader',
              exclude: /node_modules/,
              query:
                {
                  presets:['react', 'env', 'stage-1']
                }
            },
            {
              test: /\.(gif|png|jpe?g|svg)$/i,
              use: [
                'file-loader',
                {
                  loader: 'image-webpack-loader',
                  options: {
                    bypassOnDebug: true,
                  },
                },
              ],
            }
        ],
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
