import type { ScreenManager } from './ScreenManager'

export abstract class Screen {
	protected manager: ScreenManager

	constructor(manager: ScreenManager) {
		this.manager = manager
	}

	abstract render()
}
