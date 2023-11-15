import { Signal } from '@lumino/signaling';
import { ISettingRegistry } from '@jupyterlab/settingregistry';
import { IDisposable } from '@lumino/disposable';
import { DocumentRegistry } from '@jupyterlab/docregistry';
import { NotebookPanel } from '@jupyterlab/notebook';
import { postCellAlteration } from '../api';
import { EXTENSION_SETTING_NAME, Selectors } from '../utils/constants';
import { StringId } from '../utils/types';
import { isNotebookValid } from '../utils/utils';
import { CompatibilityManager } from '../utils/compatibility';

export class AlterationExtension implements DocumentRegistry.WidgetExtension {
  constructor(settings: ISettingRegistry.ISettings) {
    this._settings = settings;
  }

  createNew(panel: NotebookPanel): IDisposable {
    return new AlterationDisposable(panel, this._settings);
  }

  private _settings: ISettingRegistry.ISettings;
}

class AlterationDisposable implements IDisposable {
  constructor(panel: NotebookPanel, settings: ISettingRegistry.ISettings) {
    this._updateSettings(settings);
    settings.changed.connect(this._updateSettings.bind(this));

    panel.context.ready.then(() => {
      if (isNotebookValid(panel)) {
        this._notebookId = CompatibilityManager.getMetadataComp(
          panel.context.model,
          Selectors.notebookId
        );
        this._instanceId = CompatibilityManager.getMetadataComp(
          panel.context.model,
          Selectors.instanceId
        );
        this._cellIdList = CompatibilityManager.getCellIdsComp(
          panel.context.model.cells
        );

        // connect to notebook cell insertion/deletion/move/set
        panel.context.model.cells.changed.connect(this._onCellsAltered, this);

        // release connection
        panel.disposed.connect(this._onPanelDisposed, this);
      }
    });
  }

  private _updateSettings(settings: ISettingRegistry.ISettings) {
    this._isSettingEnabled = settings.get(EXTENSION_SETTING_NAME)
      .composite as boolean;
  }

  private _onCellsAltered = (cells: any) => {
    const newCellIdList: string[] = CompatibilityManager.getCellIdsComp(cells);
    if (this._isSettingEnabled) {
      const addedIds: string[] = newCellIdList.filter(
        item => !this._cellIdList.includes(item)
      );
      const removedIds: string[] = this._cellIdList.filter(
        item => !newCellIdList.includes(item)
      );

      for (const added_id of addedIds) {
        postCellAlteration({
          notebook_id: this._notebookId,
          instance_id: this._instanceId,
          cell_id: added_id,
          alteration_type: 'ADD',
          time: new Date().toISOString()
        });
      }
      for (const removed_id of removedIds) {
        postCellAlteration({
          notebook_id: this._notebookId,
          instance_id: this._instanceId,
          cell_id: removed_id,
          alteration_type: 'REMOVE',
          time: new Date().toISOString()
        });
      }
    }
    this._cellIdList = newCellIdList;
  };

  private _onPanelDisposed = (panel: NotebookPanel) => {
    panel.context.model.cells.changed.disconnect(this._onCellsAltered, this);
  };

  get isDisposed(): boolean {
    return this._isDisposed;
  }

  dispose(): void {
    if (this.isDisposed) {
      return;
    }

    this._isDisposed = true;
    this._notebookId = null;
    this._instanceId = null;
    this._cellIdList = [];

    Signal.clearData(this);
  }

  private _isDisposed = false;
  private _notebookId: StringId = undefined;
  private _instanceId: StringId = undefined;
  private _isSettingEnabled = false;
  private _cellIdList: string[] = [];
}
