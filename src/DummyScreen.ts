import * as termkit from 'terminal-kit'
import { Screen } from './Screen'
const term = termkit.terminal

export class DummyScreen extends Screen {
	constructor() {
		super()
	}

	async render() {
		term.green('Enter Your name: ')
		const name = await term.inputField().promise
		term.red('\n' + name)
	}
}
