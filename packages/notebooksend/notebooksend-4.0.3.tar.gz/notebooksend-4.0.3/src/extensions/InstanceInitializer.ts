import { Signal } from '@lumino/signaling';
import { v4 as uuidv4 } from 'uuid';
import { IDisposable } from '@lumino/disposable';
import { DocumentRegistry } from '@jupyterlab/docregistry';
import { NotebookPanel, INotebookModel } from '@jupyterlab/notebook';
import { Selectors } from '../utils/constants';
import { CompatibilityManager } from '../utils/compatibility';

export class InstanceInitializer
  implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel>
{
  createNew(panel: NotebookPanel) {
    return new InstanceInitializerDisposable(panel);
  }
}

class InstanceInitializerDisposable implements IDisposable {
  constructor(panel: NotebookPanel) {
    panel.context.ready.then(() => {
      const notebookModel = panel.context.model;

      if (
        CompatibilityManager.getMetadataComp(
          notebookModel,
          Selectors.notebookId
        )
      ) {
        // if no instance_id yet, assign a random one
        if (
          !CompatibilityManager.getMetadataComp(
            notebookModel,
            Selectors.instanceId
          )
        ) {
          CompatibilityManager.setMetadataComp(
            notebookModel,
            Selectors.instanceId,
            uuidv4()
          );
        }
      }
    });
  }

  get isDisposed(): boolean {
    return this._isDisposed;
  }

  dispose(): void {
    if (this.isDisposed) {
      return;
    }
    this._isDisposed = true;
    Signal.clearData(this);
  }

  private _isDisposed = false;
}
