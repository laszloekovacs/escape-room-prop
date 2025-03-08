// Import the EventEmitter class
const EventEmitter = require('events')

// Create an instance of EventEmitter
const appEmitter = new EventEmitter()

// Event handler for the "exit" event
appEmitter.on('exit', () => {
	console.log('Exit event received. Shutting down the app...')
	process.exit() // Exit the process
})

// Simulate other events and actions
appEmitter.on('action', message => {
	console.log(`Action performed: ${message}`)
})

// Function to listen for user input
function waitForInput() {
	process.stdin.setEncoding('utf8')
	console.log('Type an action or "exit" to quit:')

	process.stdin.on('data', input => {
		const trimmedInput = input.trim()
		if (trimmedInput === 'exit') {
			appEmitter.emit('exit') // Emit the exit event
		} else {
			appEmitter.emit('action', trimmedInput) // Emit an action event
		}
	})
}

// Start the input loop
waitForInput()
