# Models

`SimpleRC.mo` is a minimal RC circuit model for verifying that the
OpenModelica installation works.

## How to run

From this directory, using the OpenModelica Compiler (`omc`):

```bash
omc simulate.mos
```

The time constant is `tau = R*C = 1000 * 0.001 = 1s`, so the script
simulates for 5 seconds (5*tau) to show the full exponential charging
curve, reaching about 99.3% of `Vsource` by the end. If the installation
is working, this will compile and simulate the model, print the final
value of `Vc` at `stopTime=5`, and generate a `SimpleRC_res.mat` result
file.

Alternatively, open `SimpleRC.mo` in OMEdit (the OpenModelica graphical
IDE) and click "Simulate".

## Viewing results in Codespaces

Codespaces has no display server, so OMEdit's native plot window can't be
shown directly. Instead, `plot_result.py` reads the `.mat` result file and
renders a PNG chart that you can preview right in the VS Code editor.

```bash
pip install DyMat matplotlib scipy
python3 plot_result.py SimpleRC_res.mat Vc Vc.png
```

Then open `Vc.png` in the file explorer to view the chart inline.
