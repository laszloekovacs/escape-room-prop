import { Screen } from './Screen'
import { DummyScreen } from './DummyScreen'
import { StartScreen } from './StartScreen'
import term from './tk'

export class ScreenManager {
	private screen: Screen

	public constructor() {
		this.screen = new StartScreen(this)

		term.fullscreen(true)
		term.grabInput({ safe: true })
	}

	public async run() {
		term.clear()
		await this.screen.render()
	}

	public setScreen(screen: Screen) {
		this.screen = screen
	}

	public exit() {
		term.processExit(0)
	}
}
