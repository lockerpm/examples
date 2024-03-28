using Locker;
using Environment = Locker.Environment;

namespace LockerExample
{
    public class Program
    {
        public static void Main(string[] args)
        {
            LockerConfiguration.Instance.Init();

            EnvironmentService envService = new EnvironmentService();
            SecretService secretService = new SecretService();
            RequestOptions requestOptions = new RequestOptions()
            {
                IsJson = true
            };

            EnvironmentCreateOptions stagingEnvOpts = new EnvironmentCreateOptions()
            {
                Name = "staging",
                ExternalUrl = "staging.com",
                Description = "Staging environment"
            };
            EnvironmentCreateOptions productEnvOpts = new EnvironmentCreateOptions()
            {
                Name = "product",
                ExternalUrl = "product.com",
                Description = "Product environment"
            };


            // Create environments: staging and product
            Environment stagingEnv = (Environment)envService.Create(stagingEnvOpts, requestOptions);
            Environment productEnv = (Environment)envService.Create(productEnvOpts, requestOptions);

            // Create secret for each environment
            SecretCreateOptions secretStagingOpts = new SecretCreateOptions()
            {
                Key = "host",
                Value = "staging_host",
                Description = "Host for staging environment",
                EnvironemntName = "staging"
            };
            SecretCreateOptions secretProductOpts = new SecretCreateOptions()
            {
                Key = "host",
                Value = "product_host",
                Description = "Host for product environment",
                EnvironemntName = "product"
            };
            var hostStaging = secretService.Create(secretStagingOpts);
            var hostProduct = secretService.Create(secretProductOpts);

            Console.WriteLine($"staging env: {stagingEnv}");
            Console.WriteLine($"product env: {productEnv}");
            Console.WriteLine($"secret host staging: {hostStaging}");
            Console.WriteLine($"secret host product: {hostProduct}");

            // Retrieve secret
            var hostStagingValue = secretService.GetSecret("host", defaultValue: "", environmentName: "staging");
            var hostProductValue = secretService.GetSecret("host", defaultValue: "", environmentName: "product");

            Console.WriteLine($"Host value of staging environment: {hostStagingValue}");
            Console.WriteLine($"Host value of product environment: {hostProductValue}");
        }
    }
}