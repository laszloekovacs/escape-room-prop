import { ScreenManager } from './ScreenManager'
import { Screen } from './Screen'
import term from './tk'

export class BootScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	async render() {
		term.slowTyping('memória ellenörzés...\n')
		term.slowTyping('csatlakozás hálózathoz...\n')
		term.slowTyping('a Kremlin értesítése...\n')
	}
}
