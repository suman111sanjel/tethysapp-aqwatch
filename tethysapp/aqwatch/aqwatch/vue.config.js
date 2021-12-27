const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const {CleanWebpackPlugin} = require('clean-webpack-plugin');

module.exports = {
    outputDir: path.resolve(__dirname, '../public/build'),
    chainWebpack: (config) => {
        if (process.env.NODE_ENV === 'production') {
            // If you wish to remove the standard entry point
            config.entryPoints.delete('app')

            // then add your own
            config.entry('emission')
                .add('./src/emission.js')
                .end()
                .entry('outlook')
                .add('./src/outlook.js')
                .end()
            config.module.rule('fonts').use('url-loader')
                .loader('file-loader') // replaces the url-loader
                .tap(options => Object.assign(options, {
                    name: 'static/aqwatch/fonts/[name].[ext]'
                }))
            config.module.rule('images').use('url-loader')
                .loader('file-loader') // replaces the url-loader
                .tap(options => Object.assign(options, {
                    name: 'static/aqwatch/images/[name].[ext]'
                }))
            config.module.rule('svg').use('file-loader')
                .tap(options => Object.assign(options, {
                    name: 'static/aqwatch/images/[name].[ext]'
                }))
        }
    },
    css: {
        extract: {
            filename: 'static/aqwatch/css/[name].[contenthash].css',
            chunkFilename: 'static/aqwatch/css/chunkName.[name].[contenthash].css',
        },
    },
    configureWebpack: {
        output: {
            filename: 'static/aqwatch/js/[name].[hash].js',
            chunkFilename: 'static/aqwatch/js/[name].[hash].js',
        },
        plugins: [
            new CleanWebpackPlugin(),
        ],
    },
    pages: {
        'apps/aqwatch/emission': {
            entry: 'src/emission.js',
            template: 'public/index.html',
            filename: process.env.NODE_ENV === "production" ? '../../templates/aqwatch/Created_emission.html' : 'apps/aqwatch/emission.html',
            title: 'Air Quality Watch - Emission',
            chunks: ['chunk-vendors', 'chunk-common', 'apps/aqwatch/emission']
        },
        'apps/aqwatch/outlook': {
            entry: 'src/outlook.js',
            template: 'public/index.html',
            filename: process.env.NODE_ENV === "production" ? '../../templates/aqwatch/Created_outlook.html' : 'apps/aqwatch/outlook.html',
            title: 'Air Quality Watch',
            chunks: ['chunk-vendors', 'chunk-common', 'apps/aqwatch/outlook']
        },
    }
}
