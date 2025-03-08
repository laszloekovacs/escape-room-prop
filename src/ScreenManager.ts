import { Screen } from './Screen'
import { StartScreen } from './StartScreen'
import term from './tk'
import * as readline from 'node:readline'

export class ScreenManager extends EventTarget {
	private screen: Screen
	private rl: typeof readline

	public constructor() {
		super()
		this.screen = new StartScreen(this)
		const rl = readline.createInterface({
			input: process.stdin,
			output: process.stdout
		})
		term.fullscreen(true)
		term.grabInput({ safe: true })

		this.addEventListener('exit', () => {
			term.processExit(0)
		})
	}

	public start() {
		term.clear()
		this.screen.render()
	}

	public setScreen(screen: Screen) {
		this.screen = screen
		term.clear()
		this.screen.render()
	}
}
