import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class procontroller {
    @RequestMapping("/hello")
public String hello(){
   
    return"heelo worls";
}
}
