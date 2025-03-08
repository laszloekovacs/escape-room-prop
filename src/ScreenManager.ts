import type { Screen } from './Screen'

export class ScreenManager {
	private static instance: ScreenManager
	private screen: Screen

	private constructor(initialScreen: Screen) {
		this.screen = initialScreen
	}

	public static getInstance(initialScreen: Screen): ScreenManager {
		if (!ScreenManager.instance) {
			ScreenManager.instance = new ScreenManager(initialScreen)
		}
		return ScreenManager.instance
	}

	public run() {
		this.screen.render()
	}

	public setScreen(screen: Screen) {
		this.screen = screen
	}
}
