import { Screen } from './Screen'

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
