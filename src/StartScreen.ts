import { BootScreen } from './BootScreen'
import { Screen } from './Screen'
import { ScreenManager } from './ScreenManager'
import term from './tk'

export class StartScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	public async render() {
		const line1 = 'alvó üzemmód'
		const line2 = 'kezdéshez nyomjon meg egy billentyűt'
		const width = term.width

		const centeredLine1 = line1
			.padStart((width + line1.length) / 2)
			.padEnd(width)
		const centeredLine2 = line2
			.padStart((width + line2.length) / 2)
			.padEnd(width)

		// clear a few lines
		term.move(0, 5)
		term.gray(centeredLine1)
		term.gray(centeredLine2)
		term.nextLine(1)
		term.move(term.width / 2, 0)

		// wait for input
		//term.inputField
		await new Promise(resolve => {
			term.on('key', () => {
				resolve(true)
			})
		})
	}
}
