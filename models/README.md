# Models

`SimpleRC.mo` is a minimal RC circuit model for verifying that the
OpenModelica installation works.

## How to run

From this directory, using the OpenModelica Compiler (`omc`):

```bash
omc simulate.mos
```

If the installation is working, this will compile and simulate the model
and print the final value of `Vc` at `stopTime=0.01`, along with a
generated `SimpleRC_res.mat` result file.

Alternatively, open `SimpleRC.mo` in OMEdit (the OpenModelica graphical
IDE) and click "Simulate".
