program AmoutOfAngles;
// uses crt; 
var n, t:Integer; Angle, SumOfAngles, AngleAm, degree, fr:real;
const limit1 = 179.999; anlimd = 3; minim = 60;
begin
  writeln('What do we need to find:');
  writeln('angle(1), sum of angles(2) or how many angles(3)?');
  writeln('Amount of angles is n');
  writeln('');
  repeat
    writeln('Enter number: ');
    read(t);
    if (t > 3) or (t <= 0) then
      begin
        writeln('Retry !');
      end;
  until (t <= 3) and (t > 0); 
  if (t >= 1) and (t < 3) then
    begin
      writeln('How many angles does figure has?');
      repeat
        writeln('Enter number from ', anlimd, ' to 100:');
        read(n);
        if (n > 1000000) or (n < anlimd) then
          begin
            writeln('Retry!');
          end;
      until (n <= 1000000) and (n >= anlimd);
    end
  else 
    begin
      writeln('How many degrees does angle has?');
      repeat
    writeln('Enter from 60 to 179,999');
    read(degree);
    if (degree < minim) or (degree > limit1) then
      begin
        writeln('Retry!');
      end;
  until (degree >= minim) and (degree <= limit1);
    end;
  
  if t = 1 then
    begin
      writeln('Now lets find an angle:');
      writeln('');
      angle:=((n-2)/n)*180;
      writeln('angle=((', n, '-2)/', n, ')*180');
      writeln('angle=(', n-2, '/', n, ')*180');
      writeln('angle=', angle);
      fr:=0; 
    end
  else
    if t = 2 then
      begin
        writeln('Now lets find sum of angles:');
        writeln('');
        SumOfAngles:=(n-2)*180;
        writeln('Sum Of Angles=(', n, '-2)*180');
        writeln('Sum Of Angles=', n-2, '*180');
        writeLn('Sum of angles=', SumOfAngles);
        fr:=0;
      end
    else
      begin
        writeln('Now lets find out');
        writeln('how many angles does figure has,');
        writeln('if angles has ', degree, ' degrees:');
        writeln('');
        AngleAm:=360/(180-degree);
        writeln('n=360/(180-', degree, ')');
        writeln('n=360/', 180-degree);
        fr:=frac(AngleAm);
        if fr = 0 then
          writeln('n=', AngleAm);
      end;
end.
