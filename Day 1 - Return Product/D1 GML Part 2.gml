


// Do file stuff
var file = file_text_open_read( "input.txt");

var nums = ds_list_create();

while( !file_text_eof( file)){	
	
	var num = file_text_read_real( file);
	ds_list_add( nums, num);
	file_text_readln( file);		
	
}

file_text_close( file);

var entries = ds_list_size( nums);


// Get reeeeesult
for( var n1 = 0; n1 < entries; n1++){
	
	var num1 = nums[| n1], num2, num3;
	
	for( var n2 = 0; n2 < entries; n2++){
		
		if n2 != n1 {
			
			num2 = nums[| n2];
			
			if num1 + num2 < 2020 {
			
				for( var n3 = 0; n3 < entries; n3++){
								
					if n3 != n1 && n3 != n2 {
					
						num3 = nums[| n3];	
					
						if num1 + num2 + num3 == 2020 {
						
							show_debug_message( num1 * num2 * num3);
							exit;						
						
						}					
					
					}			
				
				}
			
			}
			
		}
		
	}	
	
}

