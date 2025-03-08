import { ScreenManager } from './ScreenManager'
import { Screen } from './Screen'
import term from './tk'

export class BootScreen extends Screen {
	constructor(manager: ScreenManager) {
		super(manager)
	}

	render() {
		term
			.slowTyping(
				'memória ellenörzés...\ncsatlakozás hálózathoz...\na Kremlin értesítése...\n'
			)
			.then(() => {
				term.green('ok')
			})
	}
}
