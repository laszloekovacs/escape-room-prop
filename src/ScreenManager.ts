import { Screen } from './Screen'
import { StartScreen } from './StartScreen'
import term from './tk'

export class ScreenManager extends EventTarget {
	private screen: Screen

	public constructor() {
		super()
		this.screen = new StartScreen(this)

		term.fullscreen(true)
		term.grabInput({ safe: true })

		this.addEventListener('exit', () => {
			this.exit()
		})
	}

	public async run() {
		term.clear()
		this.screen.render()
	}

	public setScreen(screen: Screen) {
		this.screen = screen
	}

	public exit() {
		term.processExit(0)
	}
}
