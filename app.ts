import { Screen } from './src/Screen'
import { ScreenManager } from './src/ScreenManager'

const manager = new ScreenManager(new Screen())

manager.run()
