import {
  ILabShell,
  ILayoutRestorer,
  JupyterFrontEndPlugin,
  JupyterFrontEnd
} from '@jupyterlab/application';
import { IFileBrowserFactory } from '@jupyterlab/filebrowser';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { ISettingRegistry } from '@jupyterlab/settingregistry';

//importing bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';
import { APP_ID, PLUGIN_ID } from './utils/constants';
import { compareVersions } from './utils/utils';
import { activateUploadNotebookPlugin } from './plugins/uploadNotebook';
import { activateDashboardPlugins } from './plugins/dashboards';
import { CompatibilityManager } from './utils/compatibility';

const activate = async (
  app: JupyterFrontEnd,
  factory: IFileBrowserFactory,
  restorer: ILayoutRestorer,
  labShell: ILabShell,
  rendermime: IRenderMimeRegistry,
  settingRegistry: ISettingRegistry
): Promise<void> => {
  console.log(`JupyterLab extension ${APP_ID} is activated!`);

  const targetVersion = '3.1.0';
  const appNumbers = app.version.match(/[0-9]+/g);

  if (appNumbers && compareVersions(app.version, targetVersion) >= 0) {
    const jupyterVersion = parseInt(appNumbers[0]);

    await CompatibilityManager.setJupyterVersion(jupyterVersion);

    activateUploadNotebookPlugin(app, factory);

    activateDashboardPlugins(
      app,
      restorer,
      labShell,
      settingRegistry,
      rendermime
    );
  } else {
    console.log(`Use a more recent version of JupyterLab (>=${targetVersion})`);
  }
};

const plugin: JupyterFrontEndPlugin<void> = {
  id: PLUGIN_ID,
  autoStart: true,
  requires: [
    IFileBrowserFactory,
    ILayoutRestorer,
    ILabShell,
    IRenderMimeRegistry,
    ISettingRegistry
  ],
  optional: [],
  activate: activate
};

export default plugin;
