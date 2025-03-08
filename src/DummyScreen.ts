import * as termkit from 'terminal-kit'
import { Screen } from './Screen'
import { ScreenManager } from './ScreenManager'
const term = termkit.terminal

export class DummyScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	async render() {
		term.green('Enter Your name: ')
		const name = await term.inputField().promise
		term.red('\n' + name)
	}
}
