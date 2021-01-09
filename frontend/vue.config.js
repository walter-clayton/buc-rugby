module.exports = {
	devServer: {
		proxy: {
			'^/dashboard': {
				target: 'http://127.0.0.1:5000/',
				ws: true,
				changeOrigin: true,
				logLevel: 'debug'
			},
			'^/alldata': {
				target: 'http://127.0.0.1:5000/',
				ws: true,
				changeOrigin: true,
				logLevel: 'debug'
			},
		},
	},
}