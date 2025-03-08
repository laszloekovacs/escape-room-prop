import { Screen } from './Screen'
import type { ScreenManager } from './ScreenManager'

export class DummyScreen extends Screen {
	constructor() {
		super()
	}

	render(): void {
		console.log('Dummy Screen Render')
	}

	update(): void {
		console.log('Dummy Screen Update')
	}
}
