import type { ScreenManager } from './ScreenManager'

export abstract class Screen {
	constructor() {}

	abstract render(): void

	abstract update(): void
}
