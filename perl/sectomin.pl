use strict;
use warnings;
use Scalar::Util "looks_like_number";

print("Input time in seconds: ");
my $t = <STDIN>;
chomp $t;
if (! looks_like_number($t)) {
	print("No se ha ingresado un número\n");
	exit(1);
}
print(int($t / 60), ":", $t % 60, "\n");
