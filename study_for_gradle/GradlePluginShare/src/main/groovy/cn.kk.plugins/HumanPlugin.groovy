package cn.kk.plugins
import org.gradle.api.Plugin
import org.gradle.api.Project

class HumanPlugin implements Plugin<Project>{
    @Override
    void apply(Project project) {
        project.task("HumanPluginTask") {
            doLast {
                println("human plugin ...")
            }
        }
    }
}
