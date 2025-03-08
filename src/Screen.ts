import type { ScreenManager } from './ScreenManager'

export abstract class Screen {
	private manager: ScreenManager

	constructor(manager: ScreenManager) {
		this.manager = manager
	}

	abstract render(): void

	abstract update(): void
}
