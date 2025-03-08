import { DummyScreen } from './src/DummyScreen'
import { ScreenManager } from './src/ScreenManager'

const manager = ScreenManager.getInstance(new DummyScreen())

manager.run()
