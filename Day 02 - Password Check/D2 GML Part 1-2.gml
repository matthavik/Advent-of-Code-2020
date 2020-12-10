var file = file_text_open_read( "input.txt");
var p1_valid = 0;
var p2_valid = 0;

while( !file_text_eof( file)){	
	
	var line = file_text_read_string( file);
	file_text_readln( file);
	
	var range_split = string_pos( "-", line);
	var colon_split = string_pos( ":", line);
	
	var range_start = real( string_copy( line, 0, range_split - 1));	
	var range_end = real( string_copy( line, range_split + 1, colon_split - 2 - range_split));		
	var letter = string_char_at( line, colon_split - 1);	
	var test_string = string_copy( line, colon_split + 2, string_length( line) - (colon_split + 1));

	// Part 1
	var result = string_count( letter, test_string);
	if clamp( result, range_start, range_end) == result { p1_valid += 1; }

	// Part 2
	if (string_char_at( test_string, range_start) == letter) != (string_char_at( test_string, range_end) == letter) { p2_valid += 1; }

}

file_text_close( file);

show_debug_message( "P1 Valid Passwords: " + string( p1_valid));
show_debug_message( "P2 Valid Passwords: " + string( p2_valid));