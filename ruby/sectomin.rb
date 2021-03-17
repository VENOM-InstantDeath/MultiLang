def id(c)
  for i in 0..c.length-1
    if (c[i] =~ /[0-9]/).nil?
      return false
    end
  end
  return true
end

print "Input time in seconds: "
t = gets.chomp
if not id(t)
  puts "No se ha ingresado un número"
  exit 1
end
t=t.to_i
puts "#{t/60}:#{t%60}"

