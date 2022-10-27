program SquareEquation;
uses crt; 
var x, x1, x2, a, b, c, D, sD, b0, b1, b2, e, ac4, y, y1, y2:real;
    t: integer;
begin
  clrscr;
  writeln('Is it type 1 (ay⁴+by²+c=0) or type 2 (ax²+bx+c=0)?');
  repeat
    writeln('Enter number 1 or 2: ');
    read(t);
    if (t > 2) or (t<=0) then
      begin
        writeln('Retry !');
      end;
  until (t<=2) and (t>0);
  clrscr;
  if t=1 then
    begin
      writeln(' ');
      writeln('ay⁴+by²+c=0');
      writeln('y²=x');
    end;
  if t=2 then
    writeln(' ');
  writeln('ax²+bx+c=0');
  write('a=');
  read(a);
  write('b=');
  read(b);
  write('c=');
  read(c);
  ac4:=-4*a*c;
  b2:=sqr(b);
  writeln(' ');
  writeln('(', a:0:3,'x²)+(',b:0:3,'x)+(',c:0:3,')=0');
  D:=(sqr(b))+(-4*a*c);
  writeln('D=(',b:0:3,')²-4*(',a:0:3,')*(',c:0:3,')=',D:0:3);
  writeln('D=',b2:0:3,'+(',ac4:0:3,')=',D:0:3);
  sD:=sqrt(D);
  b0:=-b+sD;
  b1:=-b-sD;
  if D>0 then
    begin
    x1:=(-(b)+(sD))/(2*a);
    x2:=(-(b)-(sD))/(2*a);
      writeln('D>0.');
      writeln('x1=((-(',b:0:3,'))+(',sD:0:3,'/(',2*a:0:3,')=',x1:0:3);
      writeln('x2=((-(',b:0:3,'))-(',sD:0:3,'/(',2*a:0:3,')=',x2:0:3);
      writeln('x1=(',b0:0:3,')/(', 2*a:0:3,')=',x1:0:3);
      writeln('x2=(',b1:0:3,')/(', 2*a:0:3,')=',x2:0:3);
      writeln(' ');
      writeln('x1=',x1:0:3,'; x2=',x2:0:3,'.');
      writeln(' ');
    end
  else
    if D=0 then
      begin 
        x:=(-(b))/(2*a);
        writeln('D=0.');
        writeln('x=(-(',b:0:3,')/(',2*a:0:3,')=', x:0:3);
        writeln(' ');
        writeln('x=',x:0:3,'.');
        writeln(' ');
      end
    else
      if D<0 then
        writeln('D<0'); 
  if (t=1) and (D>0) then
    begin
      y1:=sqrt(x1);
      y2:=sqrt(x2);
      writeln(' ');
      writeln('y1=', y1:0:3,', y2=', y2:0:3,'.')
    end
  else
    if (t=1) and (D=0) then
      begin
        y:=sqrt(x);
        writeln('y=', y:0:3, '.');
      end;
end.
