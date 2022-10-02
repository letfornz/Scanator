# Scanator
Scanator is a tool used to find active Spring Boot Actuator directories, using the brute-froce attack method.

Spring Boot Actuator Exposed
Actuator endpoints allow you to monitor and interact with your Spring application. Spring Boot includes a number of built-in endpoints and you can also add your own. For example the health endpoint provides basic application health information. The following endpoints are available:

/autoconfig - Displays an auto-configuration report showing all auto-configuration candidates and the reason why they 'were' or 'were not' applied.
/beans - Displays a complete list of all the Spring beans in your application.
/configprops - Displays a collated list of all @ConfigurationProperties.
/dump - Performs a thread dump.
/heapdump - JVM heap dump information. Actually it is a binary file, you can utilize the tool named MemoryAnalyzer to analyze the file. Sometimes in this file maybe you can find PASSWORD / ACCESS_KEY / COOKIES / ACCESS_TOKEN or some sensitive information.
/env - Exposes properties from Spring's ConfigurableEnvironment.
/health - Shows application health information (a simple 'status' when accessed over an unauthenticated connection or full message details when authenticated).
/info - Displays arbitrary application info.
/metrics - Shows 'metrics' information for the current application.
/mappings - Displays a collated list of all @RequestMapping paths.
/shutdown - Allows the application to be gracefully shutdown (not enabled by default).
/pause - Allows the application to be gracefully pause (not enabled by default).
/resume - Allows the application to be gracefully resume (not enabled by default).
/trace - Displays trace information (by default the last few HTTP requests).
