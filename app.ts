import { DummyScreen } from './src/DummyScreen'
import { ScreenManager } from './src/ScreenManager'

const manager = ScreenManager.getInstance(DummyScreen)

manager.run()
