model SimpleRC
  "Simple RC circuit to verify OpenModelica installation"
  parameter Real R = 1000 "Resistance [Ohm]";
  parameter Real C = 0.001 "Capacitance [F]";
  parameter Real Vsource = 5 "Source voltage [V]";
  Real Vc(start = 0) "Capacitor voltage [V]";
equation
  R * C * der(Vc) = Vsource - Vc;
end SimpleRC;
