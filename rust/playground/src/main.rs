fn clamp(color: i32) -> i32 {
	if color < 0 { return 0; }
	if color > 255 { return 255; }
	color
}

fn rgb(r: i32, g: i32, b: i32) -> String {
	String::from(
		  if r == 0 { format!("00") } else { format!("{:X}", clamp(r)) }  + 
		&(if r == 0 { format!("00") } else { format!("{:X}", clamp(g)) }) + 
		&(if r == 0 { format!("00") } else { format!("{:X}", clamp(b)) })
	)
}


fn main() {
	println!("{}", rgb(264, 255, 0));
}