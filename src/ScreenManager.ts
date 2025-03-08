import { Screen } from './Screen'
import { DummyScreen } from './DummyScreen'

export class ScreenManager {
	private screen: Screen

	public constructor() {
		this.screen = new DummyScreen(this)
	}

	public async run() {
		await this.screen.render()
	}

	public setScreen(screen: Screen) {
		this.screen = screen
	}

	public exit() {
		process.exit(0)
	}
}
