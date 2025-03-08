import * as termkit from 'terminal-kit'
import { Screen } from './Screen'
import { ScreenManager } from './ScreenManager'
const term = termkit.terminal

export class DummyScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	async render() {
		let name: string | undefined = ''

		while (name != 'exit') {
			term.green('\nEnter Your name: ')
			name = await term.inputField().promise
			term.red('\n' + name)
		}
	}
}
