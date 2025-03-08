import type { Screen } from './Screen'

export class ScreenManager {
	screen: Screen

	constructor(initialScreen) {
		this.screen = initialScreen
	}

	render() {
		this.screen.render()
	}

	setScreen(screen) {
		this.screen = screen
	}

	run() {}
}
