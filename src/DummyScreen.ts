import { Screen } from './Screen'
import type { ScreenManager } from './ScreenManager'

export class DummyScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	render(): void {
		console.log('Dummy Screen Render')
	}

	update(): void {
		console.log('Dummy Screen Update')
	}
}
