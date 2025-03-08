import { Screen } from './Screen'
import readline from 'node:readline'

export class ScreenManager {
	private static instance: ScreenManager
	private screen: Screen
	private rl: readline.Interface

	private constructor(initialScreen: Screen) {
		this.screen = initialScreen

		// this will prevent the process to exit
		this.rl = readline.createInterface({
			input: process.stdin,
			output: process.stdout
		})
	}

	public static getInstance<T extends Screen>(
		initialScreen: new (manager: ScreenManager) => T
	): ScreenManager {
		if (!ScreenManager.instance) {
			ScreenManager.instance = new ScreenManager(
				new initialScreen(ScreenManager.instance)
			)
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
