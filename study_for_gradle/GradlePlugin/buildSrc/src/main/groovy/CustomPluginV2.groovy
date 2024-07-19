import org.gradle.api.Plugin;
import org.gradle.api.Project;

class CustomPluginV2 implements Plugin<Project> {

    @Override
    void apply(Project project) {
        project.task('CustomPluginV2Task') {
            doLast {

                println '自定义插件V2'
            }
        }
    }
}